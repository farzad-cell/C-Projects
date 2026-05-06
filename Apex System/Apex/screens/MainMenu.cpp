#include "MainMenu.h"
#include "raylib.h"
#include "../core/ScreenController.h"
#include "../engine/WindowSetup.h"

// Update Phase--------------------------------------------------------
void MainMenuUpdate()
{
    // input + logic
    // switch screen: gScreen = SCREEN_YOUR_SCREEN;
}
// Drawing Phase--------------------------------------------------------
void MainMenuDraw()
{
    ClearBackground(RAYWHITE);
    
    // draw here
    DrawRectangle(0, 0, 300, 300, BLACK);
}