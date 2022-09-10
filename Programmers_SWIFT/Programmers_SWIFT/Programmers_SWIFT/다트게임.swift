//
//  다트게임.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/10.
//

import Foundation

func 다트게임(_ dartResult:String) -> Int {
    let multipler: [String: Float] = ["S":1, "D":2, "T":3]
    
    // S: ^1, D: ^2, T: ^3  /  * -> 해당점수,이전점수 두배 / # -> 해당점수 마이너스
    // 각 점수획득에 대한 resultArr = Int배열을 만들고 계산하자
    var resultArr = Array(repeating: 0, count: 10)
    var cur = -1
 
    var flag = false
    
    for char in dartResult {
        let str = String(char)
        if let char = Int(str) {
            if flag {
                resultArr[cur] = Int(String(resultArr[cur])+str)!
                flag = false
            } else {
                cur += 1
                resultArr[cur] = char
                flag = true
            }
            continue
        }
        
        if str == "*" {
            resultArr[cur] *= 2
            if cur != 0 { resultArr[cur-1] *= 2 }
        }
        else if str == "#" {
            resultArr[cur] *= -1
        }
        
        else {
            let value = pow(Float(resultArr[cur]), multipler[str]!)
            resultArr[cur] = Int(value)
        }
        flag = false
        
        
    }
    
    // resultArr 배열을 더한것을 반환
    return resultArr.reduce(0,+)
}
