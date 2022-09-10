//
//  3진법뒤집기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/10.
//

import Foundation

func 삼진법뒤집기(_ n:Int) -> Int {
//    var arr = [Int]()
//    var number = n
//    while (number != 0) {
//        arr.append(number % 3)
//        number = Int(number / 3)
//    }
//    print(arr)
//    var answer = 0
//    for (index, number) in  arr.reversed().enumerated() {
//        let dec: Float = pow(Float(3), Float(index))
//        answer += number * Int(dec)
//    }
    
    let flipToThree = String(n,radix: 3)
    print(flipToThree)
    let answer = Int(String(flipToThree.reversed()),radix:3)!
    return answer
    
    
    
}
