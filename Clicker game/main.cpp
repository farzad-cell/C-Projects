
// Created By Farzad Darwazi

#include "raylib.h"
#include "raymath.h"
#include "minigame.h"
#include "UiRender.h"
#include "ResourceImport.h"
#include <vector>
#include <string>

float fatiguecount = 0.0f;
float fatigueWidthBar = 0.0f;
GameData coinData;

// Prototypes
bool circleHitbox(float scale, float xPos, float yPos, Texture2D texture);
bool rectangleHitbox(float xPos, float yPos, float width, float height);
void moneyCompression(GameData& coinData, double &showMoney);

int main(void) {

    const int screenWidth = 390;
    const int screenHeight = 680;

    InitAudioDevice();
    InitWindow(screenWidth, screenHeight, "Clicker Game");
    SetTargetFPS(60);

    double showMoney = 0.00;

    // Import Resouces
    loadAll();

    GameScreen currentScreen = MENU;

    while (!WindowShouldClose()) {

        // Update phase------------------------------------------------------------------------------------------------------------------------------
        switch (currentScreen) {
        case MENU: {
            coinUpgrade(coinData, clickSnd, fatiguecount);
            // Coin button in menu
            if (circleHitbox(0.03f, 346, 350, coinTex)) {
                currentScreen = COIN_GAME;
                PlaySound(clickSnd);
            }
            // Age button
            if (circleHitbox(0.19f, 154, 374, ageTex)) {
                fatiguecount = 0.0f;
                PlaySound(clickSnd);
            }
            // JOBSCRN
            if (rectangleHitbox(17, 400, 40, 40)) {
                SetMouseCursor(MOUSE_CURSOR_POINTING_HAND);
                currentScreen = JOBSCRN;
                PlaySound(clickSnd);
            }
            
            // ASSETSCRN
            if (rectangleHitbox(77, 400, 40, 40)) {
                currentScreen = ASSETSCRN;
                PlaySound(clickSnd);
            }
            //RELATIONSCRN
            if (rectangleHitbox(277, 400, 40, 40)) {
                currentScreen = RELATIONSCRN;
                PlaySound(clickSnd);
            }
            // ACTIVITYSCRN
            if (rectangleHitbox(337, 400, 40, 40)) {
                currentScreen = ACTIVITYSCRN;
                PlaySound(clickSnd);
            }
            //SETTINGSSCRN
            if (rectangleHitbox(350, 0, 40, 40)) {
                currentScreen = SETTINGSCRN;
                PlaySound(clickSnd);
            }
            break;
        }
        case COIN_GAME:
			// Coin button + fatigue increase
            if (circleHitbox(0.25f, 50, 80,  coinTex)) {
                coinData.money += coinData.coinRate;
                fatiguecount += 0.1f;
                PlaySound(coinSnd);
            }
			// Upgrade button
            coinUpgrade(coinData, clickSnd, fatiguecount);
            if (coinData.money < 0)
                coinData.money = 0.00f;
			// Back button hitbox
            if(circleHitbox(0.07f, 330, 380, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;
        case JOBSCRN:
            if (circleHitbox(0.07, 0, 0, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;
        case SCHOOLSCRN:
            if (circleHitbox(0.07, 0, 0, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;
        case ASSETSCRN:
            if (circleHitbox(0.07, 0, 0, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;
        case SETTINGSCRN:
            if (circleHitbox(0.07, 0, 0, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;
        case RELATIONSCRN:
            if (circleHitbox(0.07, 0, 0, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;
        case ACTIVITYSCRN:
            if (circleHitbox(0.07, 0, 0, backTex)) {
                currentScreen = MENU;
                PlaySound(clickSnd);
            }
            break;

            }



        // Drawing phase------------------------------------------------------------------------------------------------------------------------------
        BeginDrawing();

        ClearBackground(BLACK);

        switch (currentScreen) {
        case MENU:
            fatigueWidthBar = fatigueBar(fatiguecount);
            drawMenu();
            moneyCompression(coinData, showMoney);
            break;
        case COIN_GAME:
            moneyCompression(coinData, showMoney);
            drawCOIN_GAME();
            break;
        case JOBSCRN:
            DrawRectangle(0, 0, 390, 45, GRAY);
            DrawTextureEx(backTex, { 0, 0 }, 0.0f, 0.07f, WHITE);
			break;
		case SCHOOLSCRN:
            DrawRectangle(0, 0, 390, 45, GRAY);
            DrawTextureEx(backTex, { 0, 0 }, 0.0f, 0.07f, WHITE);
			break;
		case ASSETSCRN:
            DrawRectangle(0, 0, 390, 45, GRAY);
            DrawTextureEx(backTex, { 0, 0 }, 0.0f, 0.07f, WHITE);
			break;
		case SETTINGSCRN:
            DrawRectangle(0, 0, 390, 45, GRAY);
            DrawTextureEx(backTex, { 0, 0 }, 0.0f, 0.07f, WHITE);
			break;
		case RELATIONSCRN:
            DrawRectangle(0, 0, 390, 45, GRAY);
            DrawTextureEx(backTex, { 0, 0 }, 0.0f, 0.07f, WHITE);
			break;
		case ACTIVITYSCRN:
            DrawRectangle(0, 0, 390, 45, GRAY);
            DrawTextureEx(backTex, { 0, 0 }, 0.0f, 0.07f, WHITE);
			break;
        }
        EndDrawing();      
    }
    
    void unloadAll();
  
    return 0;
}

bool circleHitbox(float scale, float xPos, float yPos, Texture2D texture) {
    Vector2 mousePos = GetMousePosition();
    
    Vector2 center = {
        xPos + (texture.width * scale) / 2.0f,
        yPos + (texture.height * scale) / 2.0f
    };
    float radius = (texture.width * scale) / 2.0f;
    
    float dist = Vector2Distance(mousePos, center);
    return (IsMouseButtonPressed(MOUSE_LEFT_BUTTON) && dist < radius); 
}

bool hoverIco(float xPos, float yPos, float width, float height) {
    return CheckCollisionPointRec(GetMousePosition(), {xPos, yPos, width, height});
}

bool rectangleHitbox(float xPos, float yPos, float width, float height) {
    Vector2 mousePos = GetMousePosition();
    Rectangle btn1 = { xPos, yPos, width, height };
    return (IsMouseButtonPressed(MOUSE_BUTTON_LEFT) && CheckCollisionPointRec(mousePos, btn1));
}

void moneyCompression(GameData& coinData, double& showMoney) {
    int sufixIndx;
	const char *suffixes[] = { "", "M", "B", "T", "Q"};

    if(coinData.money >= 1e15) {
        showMoney = coinData.money / 1e15;
        sufixIndx = 4;
    }
    else if (coinData.money >= 1e12) {
        showMoney = coinData.money / 1e12;
        sufixIndx = 3;
    }
    else if (coinData.money >= 1e9) {
        showMoney = coinData.money / 1e9;
        sufixIndx = 2;
	}
	else if (coinData.money >= 1e6) {
        showMoney = coinData.money / 1e6;
        sufixIndx = 1;
    }
    else {
        showMoney = coinData.money;
		sufixIndx = 0;
	}

    DrawText(TextFormat("$%.2f%s", showMoney, suffixes[sufixIndx]), 10, 0, 40, GOLD);
}   