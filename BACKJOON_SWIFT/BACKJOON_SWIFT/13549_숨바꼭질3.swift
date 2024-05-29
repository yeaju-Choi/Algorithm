//
//  13549_숨바꼭질3.swift
//  BACKJOON_SWIFT
//
//  Created by Nudge on 5/8/24.
//

/*
 
 5 17  // 5-10-9-18-17 순으로 가면 2초
 - 1초 후에 X-1 또는 X+1
 - 0초 후에 2*X의 위치로 이동
 

 |target - now + 1|  |target-(now*2)| // 어림도 없음
 //
비용있는 그래프 ?
 
 bfs~
 
  // 5 0
 p = [100000] * 200000.
 n, k = map(int, input().split())
 dp[n] = 0

 def find_dp(now, x):
    
     print(x, abs(k-n), x>abs(k-n), now>k*2 )
     if(now<=0 or x>abs(k-n)):
         return

     dp[now] = min(x, dp[now])
     if now == k:
         return

     print(dp[now-1]>x+1, now, x, dp[now-1])
     if (dp[now*2]>x):
         find_dp(now*2, x)
     if(now>0 and dp[now-1]>x+1):
         find_dp(now-1, x+1)
     if(now<=k*2 and dp[now+1]>x+1):
         find_dp(now+1, x+1)

 now = n
 find_dp(now, 0)

 print(dp[k])
 
 
 */

import Foundation

func sol13549() {
    
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let now = input[0]
    let target = input[1]
    var queue: [(Int, Int)] = []
    var visited = Array(repeating: false, count: 100001)
    bfs()
    // 현재 위치, 걸리는시간
    func bfs(){
        queue.append((now, 0))
        
        while !queue.isEmpty{
            let pop = queue.removeFirst()
            
            if pop.0 == target {
                print(pop.1)
                break
            }
            
            if pop.0 * 2 < 100001 && !visited[pop.0 * 2]{
                visited[pop.0 * 2] = true
                queue.append((pop.0 * 2, pop.1))

            }
            
            if pop.0 - 1 >= 0 && !visited[pop.0 - 1]{
                visited[pop.0 - 1] = true
                queue.append((pop.0 - 1, pop.1 + 1))

            }
            
            if pop.0 + 1 < 100001 && !visited[pop.0 + 1]{
                visited[pop.0 + 1] = true
                queue.append((pop.0 + 1, pop.1 + 1))

               }
               
//            print(queue)
           }
        
       }
}
