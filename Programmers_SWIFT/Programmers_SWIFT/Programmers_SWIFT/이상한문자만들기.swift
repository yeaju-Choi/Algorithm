//
//  이상한문자만들기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/27.
//

import Foundation

func 이상한문자만들기(_ s:String) -> String {
    var arr: [String] = []
    var x = 0
    for i in s {
        if x % 2 == 0 {
            arr.append(String(i.uppercased()))
        } else {
            arr.append(String(i.lowercased()))
        }
        x += 1
        if i == " " {
            x = 0
        }
    }
    return arr.joined()
}
