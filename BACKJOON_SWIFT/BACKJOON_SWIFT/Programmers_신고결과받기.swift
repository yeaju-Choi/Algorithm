//
//  Programmers_신고결과받기.swift
//  BACKJOON_SWIFT
//
//  Created by 최예주 on 2022/07/11.
//

import Foundation


// { 신고당한사람1 : [신고한사람1, 신고한사람2,,], 신고당한사람2 : [신고한사람,..] , .. } 으로 저장
// 딕셔너리의 Value를 Set으로 설정하면 중복 검사 로직을 없앨 수 있다!
//

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    
    // 정답을 담을 딕셔너리
    var answer: [String:Int] = Dictionary()
    for user in id_list {
        answer[user] = 0
    }
    
    var reportDict: [String: Set<String>] = Dictionary()
    for user in id_list{
        reportDict[user] = Set<String>()
    }
    
    
//    print(reportDict)
    
    // "muzi frodo" 이런식으로 [신고한 사람 신고당한사람] 들어오기때문에 공백 기준으로 나누어 딕셔너리에 저장해줌
    for name in report{
        var reportString = name.split(separator: " ")
        let reporter:String = String(reportString[0])
        let reported:String = String(reportString[1])
        
//        guard !((reportDict[reported]?.contains(reporter))!) else { continue }
//        reportDict[reported]?.append(reporter)
        reportDict[reported]?.insert(reporter)
    }

//    print(reportDict)
    
    
    // 딕셔너리 value 갯수가 k 이상이면 정답 딕셔너리에 1씩 + !
    reportDict.map { reported, reporter in
        if reporter.count >= k {
            for user in reporter{
                answer[user]! += 1
            }
        }
    }
    
    var realAnswer:[Int] = []
    print(Array(answer.values))
    
   
//    [2,1,1,0]
    return []
    }


