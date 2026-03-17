// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SkillSwapExecutor {

    event SwapExecuted(
        address tokenIn,
        address tokenOut,
        uint amountIn,
        uint amountOut
    );

    function executeSwap(
        address tokenIn,
        address tokenOut,
        uint amountIn
    ) external {

        // placeholder logic

        emit SwapExecuted(tokenIn, tokenOut, amountIn, 0);
    }
}
