//
//  12919_A와B2.swift
//  BACKJOON_SWIFT
//
//  Created by Nudge on 5/7/24.
//

// https://www.acmicpc.net/problem/12919

/*
 
 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다. 문자열을 바꿀 때는 다음과 같은 두 가지 연산만 가능하다.
 - 문자열의 뒤에 A를 추가한다.
 - 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
 주어진 조건을 이용해서 S를 T로 만들 수 있는지 없는지 알아내는 프로그램을 작성하시오.
 
 ==
 첫째 줄에 S가 둘째 줄에 T가 주어진다. (1 ≤ S의 길이 ≤ 49, 2 ≤ T의 길이 ≤ 50, S의 길이 < T의 길이)
 ==
 
 S를 T로 바꿀 수 있으면 1을 없으면 0을 출력한다.
 
 */

// 시간초과 ;

//
import Foundation


func sol12919() {
    var s = readLine()!.map{ String($0) }
    let t = readLine()!.map{ String($0) }
    
    print(recursive(arr: s) + reversedAndAppendB(arr: s))

    func recursive(arr: [String]) -> Int {
        if arr == t {
            print(1)
            exit(0)
        }
        if arr.count >= t.count {
            return 0
        }
        
        var tempArr = arr
        tempArr.append("A")
        
        return recursive(arr: tempArr) + reversedAndAppendB(arr: tempArr)
    }
    
    func reversedAndAppendB(arr: [String]) -> Int {
        if arr == t {
            print(1)
            exit(0)
        }
        if arr.count >= t.count {
            return 0
        }
        
        var tempArr = arr
        tempArr.append("B")
        tempArr.reverse()
        return recursive(arr: tempArr) + reversedAndAppendB(arr: tempArr)
    }
    
    
}
