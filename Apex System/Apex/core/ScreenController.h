#pragma once

#ifndef SCREENCONTROLLER_H
#define SCREENCONTROLLER_H

typedef enum
{
    SCREEN_MAIN_MENU
} AppScreen;

extern AppScreen gScreen;

void ScreenUpdate();
void ScreenDraw();

#endif