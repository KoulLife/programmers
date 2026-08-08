import copy

# [[160, 140, 120, 110, 60], [40, 2, 3]
# [290, 270, 260, 120, 10], [40, 5, 3]
# [160, 130, 120, 60, 20], [20, 5, 4],
# [160, 120, 80, 70, 20], [50, 5, 5]
# [110, 70, 60, 30, 20]]

# 풀이 생각: 힌트 비용 보다 힌트 사용해서 얻는 이점이 크다면 구매.
# 아니면 무식하게 산다, 안산다로 다 돌리면 될까?

def solution(cost, hint):
    step = len(cost)
    res = float('inf')

    def simulation_cost(s_step, hint_history, val):
        nonlocal res

        if s_step == step:
            res = min(res, val)
            return

        # 현재 스테이지에서 가지고 있는 힌트 개수
        hint_count = hint_history.get(s_step, 0)
        hint_count = min(hint_count, step - 1)

        # 현재 스테이지 해결 비용
        val += cost[s_step][hint_count]

        # 1. 힌트 번들을 안 산다
        simulation_cost(s_step + 1, hint_history, val)

        # 2. 힌트 번들을 산다
        if s_step < len(hint):
            step_hint = hint_history.copy()

            # hint[s_step][0]은 가격
            # hint[s_step][1:]이 얻는 힌트 번호들
            for v in hint[s_step][1:]:
                idx = v - 1

                step_hint[idx] = min(
                    step - 1,
                    step_hint.get(idx, 0) + 1
                )

            simulation_cost(
                s_step + 1,
                step_hint,
                val + hint[s_step][0]
            )

    simulation_cost(0, {}, 0)

    return res
    