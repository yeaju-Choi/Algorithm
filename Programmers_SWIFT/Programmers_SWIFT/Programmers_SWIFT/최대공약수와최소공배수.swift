//
//  최대공약수와최소공배수.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/23.
//

import Foundation

// 유클리드 호제법으로 풀기~,~ 외워두면 편할것 같다.
func GCD(_ n: Int, _ m: Int) -> Int {
    if m == 0 {
        return n
    } else {
        return GCD(m, n%m)
    }
}

func LCM(_ n: Int, _ m: Int) -> Int {
    return n * m / GCD(n, m)
}

func 최대공약수와최소공배수(_ n:Int, _ m:Int) -> [Int] {
    return [GCD(n,m), LCM(n, m)]
}
