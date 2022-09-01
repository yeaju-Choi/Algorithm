//
//  문자열다루기기본.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/01.
//

import Foundation

func 문자열다루기기본(_ s:String) -> Bool {
    return (s.count == 4 || s.count == 6) && ((Int(s)) != nil)
}
