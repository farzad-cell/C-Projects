#include "raylib.h"
#include "UiRender.h"
#include "ResourceImport.h"
#include "minigame.h"

// For Drawing the UI

void drawMenu() {
    bool hover1 = hoverIco(17, 400, 40, 40);
    bool hover2 = hoverIco(77, 400, 40, 40);
    bool hover3 = hoverIco(277, 400, 40, 40);
    bool hover4 = hoverIco(337, 400, 40, 40);

    DrawRectangle(0, 420, 390, 350, GRAY);
    DrawRectangle(0, 0, 390, 80, GRAY);
    // Balance text
    DrawTextureEx(coinTex, { 346, 350 }, 0.0f, 0.03f, WHITE);
    DrawRectangle(0, 385, 400, 70, BLUE);
    DrawCircle(200, 420, 45, WHITE);
    DrawTextureEx(ageTex, { 138, 360 }, 0.0f, 0.25f, WHITE);
    DrawRectangle(60, 500, 300, 20, WHITE);
    DrawRectangle(60, 500, static_cast<int>(fatigueWidthBar), 20, RED);
    DrawTextureEx(sleepTex, { 10, 490 }, 0.0f, 0.07f, WHITE);
    DrawTextureEx(jobTex, { 20, 405 }, 0.0f, 0.05f, hover1 ? BLACK : WHITE);
    DrawTextureEx(assetTex, { 80, 405 }, 0.0f, 0.05f, hover2 ? BLACK : WHITE);
    DrawTextureEx(relationTex, { 280, 405 }, 0.0f, 0.05f, hover3 ? BLACK : WHITE);
    DrawTextureEx(activityTex, { 340, 405 }, 0.0f, 0.05f, hover4 ? BLACK : WHITE);
    DrawTextureEx(settingsTex, { 355, 5 }, 0.0f, 0.05f, WHITE);
    DrawTextEx(fontLight, "Energy", { 60, 500 }, 20, 1.0f, BLACK);

    // Icon hitbox locator
    //DrawRectangleLines(350, 0, 40, 40, RED);
}

void drawCOIN_GAME() {
    // Balance text in coin game
    DrawTextureEx(coinTex, { 50, 80 }, 0.0f, 0.25f, WHITE);
    DrawText(TextFormat("%.2f", coinData.coinCost[coinData.coinIndex]), 10, 430, 20, WHITE);
    DrawTextureEx(backTex, { 330, 380 }, 0.0f, 0.07f, WHITE);
    DrawRectangle(50, 50, 300, 20, WHITE);
    fatigueWidthBar = fatigueBar(fatiguecount);
    DrawRectangle(50, 50, static_cast<int>(fatigueWidthBar), 20, RED);
}