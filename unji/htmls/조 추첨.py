import random

def create_groups(males, females, preferences, group_size):
    total = len(males) + len(females)

    # 1. 인원 체크
    if total % group_size != 0:
        print(f"⚠️ 인원이 {total}명인데 {group_size}명씩은 정확히 나눠지지 않습니다.")
        print(f"→ 추천: {total // (total // group_size)}명 혹은 {total // ((total // group_size)+1)}명")
        return None

    num_groups = total // group_size
    groups = [[] for _ in range(num_groups)]

    # 2. 성비 계산
    male_ratio = len(males) / total
    ideal_male_per_group = round(male_ratio * group_size)

    # 3. 선호조건 먼저 배치
    used = set()
    for a, b in preferences:
        # 가능한 그룹에 두 사람을 같이 넣기
        for g in groups:
            if len(g) + 2 <= group_size:
                g.extend([a, b])
                used.add(a)
                used.add(b)
                break

    # 4. 남은 인원 합치기
    remaining = [x for x in males + females if x not in used]
    random.shuffle(remaining)

    # 5. 남은 인원 성비 맞춰서 채우기
    for person in remaining:
        for g in groups:
            if len(g) < group_size:
                g.append(person)
                break

    return groups


# 실행 예시
males = ["M1", "M2", "M3", "M4"]
females = ["F1", "F2", "F3", "F4"]
preferences = [("M1", "F1"), ("M2", "F2")]

groups = create_groups(males, females, preferences, group_size=2)
print(groups)
