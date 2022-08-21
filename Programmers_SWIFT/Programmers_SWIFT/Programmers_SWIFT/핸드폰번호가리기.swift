//
//  핸드폰번호가리기.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/21.
//

import Foundation

func 핸드폰번호가리기(_ phone_number:String) -> String {
    var answer = ""

    for (index,char) in phone_number.reversed().enumerated() {
        if index > 3 { answer.append("*")} else {
            answer.append(char)
        }
    }

    return String(answer.reversed())
    
    // MARK: Other Answer => suffix 함수 이용
//    return String(repeating: "*", count: phone_number.count - 4) + phone_number
}
