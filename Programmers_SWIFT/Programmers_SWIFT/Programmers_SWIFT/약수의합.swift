//
//  약수의합.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/28.
//

import Foundation

func 약수의합(_ n:Int) -> Int {
    if n == 0 { return 0 }
    var answer = 0
    for num in Array(1...n).reversed() {
        if n % num == 0 {
            answer += num
        }
    }
    return answer
    
    // filter, reduce 사용
//    return Array(1...n).filter { n % $0 == 0 }.reduce(0,+)
}
