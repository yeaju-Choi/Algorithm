//
//  15989_1,2,3더하기4.swift
//  BACKJOON_SWIFT
//
//  Created by Nudge on 5/9/24.
//
/*
 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

 - 1+1+1+1
 - 2+1+1 (1+1+2, 1+2+1)
 - 2+2
 - 1+3 (3+1)
 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
 
 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 10,000보다 작거나 같다.
 
 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
 
 */
import Foundation

func sol15989() {
    let t = Int(String(readLine()!))!
    var dp = Array(repeating: Array(repeating: 0, count: 3), count: 10001)
    dp[1][0] = 1
    dp[2][0] = 1
    dp[2][1] = 1
    dp[3][0] = 1
    dp[3][1] = 1
    dp[3][2] = 1
//    print(dp)
    for i in stride(from: 4, to: 10001, by: 1){
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 2][1] + dp[i - 2][0]
        dp[i][2] = dp[i - 3][0] + dp[i - 3][1] + dp[i - 3][2]
    }
    for i in dp {
        print(i)
    }
    for _ in 0..<t{
        let a = Int(String(readLine()!))!
        print(dp[a][0] + dp[a][1] + dp[a][2])
    }
}
