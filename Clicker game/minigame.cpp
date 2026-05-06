
#include "minigame.h"
#include "raylib.h"


void coinUpgrade(GameData &coinData, Sound clickSnd, float &fatiguecount) {

    // Coin upgrade button
    if (rectangleHitbox(10, 430, 100, 25)) {
        if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            if (coinData.coinIndex < coinUpgradeSize && coinData.money >= coinData.coinCost[coinData.coinIndex] - 0.001f) {
                coinData.money -= coinData.coinCost[coinData.coinIndex];
                coinData.coinRate = coinData.coinPower[coinData.coinIndex];
                coinData.coinIndex++;
                PlaySound(clickSnd);
            }
        }
    }
}


float fatigueBar(float &fatiguecount) {
    float currentWidth;
	float maxWidth = 300.0f;
	float maxFatigue = 100.0f;

	currentWidth = maxWidth * (fatiguecount / maxFatigue);

    if(currentWidth > maxWidth) {
        currentWidth = maxWidth;
	}
	return currentWidth;
}