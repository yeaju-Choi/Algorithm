//
//  2577_숫자의개수.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/02/03.
//

import Foundation

func sol2577(){
    
    let a = Int(readLine()!)!
    let b = Int(readLine()!)!
    let c = Int(readLine()!)!

    let mul = String(a*b*c)
    var answerArr = Array(repeating: 0, count: 10)

    mul.forEach {
        answerArr[Int(String($0))!] += 1
    }

    answerArr.forEach {
        print($0)
    }
}



