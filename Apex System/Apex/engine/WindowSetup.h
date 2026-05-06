#pragma once

#ifndef WINDOWSETUP_H
#define WINDOWSETUP_H

#include "raylib.h"
#include "raymath.h"

#define CANVAS_W 800
#define CANVAS_H 450

extern Vector2 gMouse;

void WindowInit(const char* title);
void WindowBeginFrame();
void WindowEndFrame();
void WindowShutdown();

#endif