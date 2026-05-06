#include "ScreenController.h"
#include "../screens/MainMenu.h"

AppScreen gScreen = SCREEN_MAIN_MENU;

void ScreenUpdate()
{
    switch (gScreen)
    {
    case SCREEN_MAIN_MENU: MainMenuUpdate(); break;
    }
}

void ScreenDraw()
{
    switch (gScreen)
    {
    case SCREEN_MAIN_MENU: MainMenuDraw(); break;
    }
}