//
//  시저암호.swift
//  Programmers_SWIFT
//
//  Created by 최예주 on 2022/08/28.
//

import Foundation

func 시저암호(_ s:String, _ n:Int) -> String {
    // 하나씩 요소를 꺼내서 공백이면 그대로 리턴하고, 아니라면 아스키코드로 변환
    // MARK: print(Character(UnicodeScalar(숫자))) 이용하여 아스키값을 문자로 변경
    // 문자 -> 아스키코드 변경 : UnicodeScalar("A").value
    let answer = s.map { char -> Character in
        if char != " " {
            var asciiCode = UnicodeScalar(String(char))!.value + UInt32(n)
            
            if (asciiCode > 122 && char.isLowercase) || (asciiCode > 90 && char.isUppercase) {
                asciiCode -= 26
            }
            
            return Character(UnicodeScalar(asciiCode)!)
        }
        return Character(" ")
    }
    return String(answer)
    
}
