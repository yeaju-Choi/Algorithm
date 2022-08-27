//
//  정수내림차순으로배치하기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/27.
//

import Foundation

func 정수내림차순으로배치하기(_ n:Int64) -> Int64 {
    let arr = String(n).sorted(by: >)
    return Int64(String(arr))!
}
