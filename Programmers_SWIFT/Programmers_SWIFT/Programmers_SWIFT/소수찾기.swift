//
//  소수찾기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/01.
//

import Foundation

func 소수찾기(_ n:Int) -> Int {
    // 에라토스테스체 알고리즘 적용
    var arr = Array(repeating: true, count: n+1)
    var primes = [Int]()
    arr[0] = false
    arr[1] = false
    
    for i in 0...n {
        if arr[i] {
            for j in stride(from: i, through: n, by: i) {
                print(j, i)
                if j % i == 0 {
                    arr[j] = false
                }
            }
            primes.append(i)
        }
    }    
    return primes.count
    
    
}
