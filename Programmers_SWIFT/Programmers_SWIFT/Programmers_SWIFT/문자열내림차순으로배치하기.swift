//
//  문자열내림차순으로배치하기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/09/01.
//

import Foundation

func 문자열내림차순으로배치하기(_ s:String) -> String {
    return String(s.sorted(by: >))
}
