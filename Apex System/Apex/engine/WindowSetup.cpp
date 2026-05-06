#include "WindowSetup.h"

static RenderTexture2D gCanvas;
static Rectangle       gSourceRec;
static Rectangle       gDestRec;
static Vector2         gOrigin;
Vector2                gMouse = { 0.0f, 0.0f };

static Rectangle ComputeDestRec()
{
    Rectangle r;
    r.x = 0.0f;
    r.y = 0.0f;
    r.width = (float)GetScreenWidth();
    r.height = (float)GetScreenHeight();
    return r;
}

static void UpdateMouse()
{
    Vector2 raw = GetMousePosition();
    float   scale = gDestRec.width / (float)CANVAS_W;
    gMouse.x = Clamp((raw.x - gDestRec.x) / scale, 0.0f, (float)(CANVAS_W - 1));
    gMouse.y = Clamp((raw.y - gDestRec.y) / scale, 0.0f, (float)(CANVAS_H - 1));
}

void WindowInit(const char* title)
{
    SetConfigFlags(FLAG_WINDOW_RESIZABLE | FLAG_VSYNC_HINT | FLAG_WINDOW_HIGHDPI);
    InitWindow(CANVAS_W, CANVAS_H, title);

    gCanvas = LoadRenderTexture(CANVAS_W, CANVAS_H);
    SetTextureFilter(gCanvas.texture, TEXTURE_FILTER_BILINEAR);

    gSourceRec.x = 0.0f;
    gSourceRec.y = 0.0f;
    gSourceRec.width = (float)CANVAS_W;
    gSourceRec.height = -(float)CANVAS_H;

    gOrigin.x = 0.0f;
    gOrigin.y = 0.0f;

    gDestRec = ComputeDestRec();
}

void WindowBeginFrame()
{
    if (IsWindowResized()) gDestRec = ComputeDestRec();
    UpdateMouse();
    BeginTextureMode(gCanvas);
}

void WindowEndFrame()
{
    EndTextureMode();
    BeginDrawing();
    ClearBackground(BLACK);
    DrawTexturePro(gCanvas.texture, gSourceRec, gDestRec, gOrigin, 0.0f, WHITE);
    EndDrawing();
}

void WindowShutdown()
{
    UnloadRenderTexture(gCanvas);
    CloseWindow();
}