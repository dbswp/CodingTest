function calculateRainwater(blocks) {
    const n = blocks.length;
    let totalWater = 0;
  
    // 왼쪽과 오른쪽 최대 높이 배열 초기화
    const leftMax = new Array(n).fill(0);
    const rightMax = new Array(n).fill(0);
  
    // 왼쪽 벽의 최대 높이 계산
    leftMax[0] = blocks[0];
    for (let i = 1; i < n; i++) {
      leftMax[i] = Math.max(leftMax[i - 1], blocks[i]);
    }
  
    // 오른쪽 벽의 최대 높이 계산
    rightMax[n - 1] = blocks[n - 1];
    for (let i = n - 2; i >= 0; i--) {
      rightMax[i] = Math.max(rightMax[i + 1], blocks[i]);
    }
  
    // 빗물 계산
    for (let i = 0; i < n; i++) {
      const minHeight = Math.min(leftMax[i], rightMax[i]);
      if (minHeight > blocks[i]) {
        totalWater += minHeight - blocks[i];
      }
    }
  
    return totalWater;
  }
  
  // 예시 입력: [0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0]
  const blocks = [0, 2, 0, 1, 3, 1, 2, 0, 1, 0, 2, 0];
  const rainwater = calculateRainwater(blocks);
  
  console.log(rainwater); 