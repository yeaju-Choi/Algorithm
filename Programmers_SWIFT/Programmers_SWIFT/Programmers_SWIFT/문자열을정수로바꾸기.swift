//
//  문자열을정수로바꾸기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/01.
//

import Foundation

func 문자열을정수로바꾸기(_ s:String) -> Int {
    // MARK: 그냥 Int("-1234")! 도 가능하구나..
    if s.first! == "+" {
        return Int(s.suffix(s.count-1))!
    } else if s.first! == "-" {
        return Int(s.suffix(s.count-1))! * -1
    }
    return Int(s)!
    // return Int(s)!
}
