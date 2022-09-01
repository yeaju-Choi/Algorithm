//
//  수박수박수박수박수박수.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/01.
//

import Foundation


func 수박수박수박수박수박수(_ n:Int) -> String {
    let arr = ["수","박"]
    var answer = ""
    for i in 0..<n {
        answer += arr[i % 2]
    }
    return answer
    // another answer
    // return (0..<n).map{($0%2==0 ? "수":"박")}.reduce("", +)
}
