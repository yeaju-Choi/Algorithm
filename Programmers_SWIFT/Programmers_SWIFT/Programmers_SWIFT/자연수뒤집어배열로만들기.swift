//
//  자연수뒤집어배열로만들기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/27.
//

import Foundation

func 자연수뒤집어배열로만들기(_ n:Int64) -> [Int] {
    return String(n).reversed().map{Int(String($0))!}
}
