//
//  20055.swift
//  BACKJOON_SWIFT
//
//  Created by Nudge on 5/25/24.
//

/*
 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
 
 */
import Foundation

func sol20055() {

    struct Blank {
        var life: Int
        var hasRobot: Bool
    }

    let nk = readLine()!.split(separator: " ").map { Int($0)! }
    let n = nk[0]
    let k = nk[1]
    var convainer: [Blank] = []
    convainer = readLine()!.split(separator: " ").map { Int($0)! }.map{ .init(life: $0, hasRobot: false)}
    var answer = 0
    var zeroBlankCount = 0

    func lotateConvainer() {
        convainer.insert(convainer.removeLast(), at: 0)
    }

    func countZeroBlank() {
        var count = 0
        convainer.forEach { blank in
            if blank.life == 0 {
                count += 1
            }
        }
        zeroBlankCount = count
    }

    while zeroBlankCount < k {
        answer += 1
        lotateConvainer()
        if convainer[n-1].hasRobot {
            convainer[n-1].hasRobot = false
        }
        for i in stride(from: n-2, through: 0, by: -1) {
            if convainer[i].hasRobot && convainer[i+1].life >= 1 && !convainer[i+1].hasRobot {
                convainer[i+1].life -= 1
                convainer[i].hasRobot = false
                if i == n-2 {
                    continue
                }
                convainer[i+1].hasRobot = true
            }
        }
        if convainer[0].life >= 1 && !convainer[0].hasRobot {
            convainer[0].hasRobot = true
            convainer[0].life -= 1
        }
        countZeroBlank()
    }

    print(answer)
}
