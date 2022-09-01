//
//  문자열내p와y의개수.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/01.
//

import Foundation

func 문자열내p와y의개수(_ s:String) -> Bool {
    var pCount = 0
    var yCount = 0
    s.forEach { char in
        if char == Character("p") || char == Character("P") { pCount += 1 }
        if char == Character("y") || char == Character("Y") { yCount += 1 }
    }
    return pCount == yCount
    // another answer
    // return s.lowercased().filter { $0 == "p" }.count == s.lowercased().filter { $0 == "y" }.count
}
