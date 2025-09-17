<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>스택을 활용한 게임 HP 관리 시스템</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #eee;
            margin-bottom: 20px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        h1 {
            font-size: 2.5em;
        }
        h2 {
            font-size: 1.8em;
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
            margin-top: 40px;
        }
        .code-block {
            background-color: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre {
            margin: 0;
        }
        p {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>스택을 활용한 게임 HP 관리 시스템</h1>
            <p>데이터의 흐름을 통제하는 자료구조의 힘</p>
        </header>

        <section>
            <h2>개요</h2>
            <p>
                게임에서 캐릭터의 체력(HP) 관리는 매우 중요합니다. 이 프로젝트는 단순한 값의 증감 대신, 스택(Stack)이라는 자료구조를 사용하여 HP 변화의 **이력을 기록하고 관리**하는 시스템을 구현합니다. 이를 통해 사용자에게 '되돌리기(Undo)'와 같은 고급 기능을 제공할 수 있습니다.
            </p>
            <p>
                스택은 **LIFO(Last-In, First-Out)**, 즉 가장 최근에 들어온 데이터가 가장 먼저 나가는 특성을 가집니다. 이 특성을 활용하여 HP가 변경될 때마다 그 상태를 스택에 쌓고, 되돌리기 기능을 실행할 때 가장 최근 상태를 꺼내어 이전으로 복구하는 방식입니다.
            </p>
        </section>

        <section>
            <h2>파이썬 코드: HPStack 클래스</h2>
            <p>
                아래 파이썬 코드는 게임 캐릭터의 HP를 스택으로 관리하는 `HPStack` 클래스를 보여줍니다. 데미지(`take_damage`), 회복(`heal`) 함수와 더불어 가장 최근의 행동을 취소하는 `undo` 함수가 핵심입니다.
            </p>
            <div class="code-block">
                <pre>
class HPStack:
    """
    스택을 이용하여 HP 변화 이력을 관리하는 클래스입니다.
    """
    def __init__(self, initial_hp):
        self.history = [initial_hp]
        self.current_hp = initial_hp

    def take_damage(self, amount):
        """
        데미지를 받아 HP를 감소시키고, 이전 상태를 스택에 저장합니다.
        """
        if amount > 0:
            self.current_hp -= amount
            self.history.append(self.current_hp)
            print(f"데미지 {amount}를 입었습니다. 현재 HP: {self.current_hp}")
        else:
            print("데미지 값은 양수여야 합니다.")

    def heal(self, amount):
        """
        HP를 회복시키고, 이전 상태를 스택에 저장합니다.
        """
        if amount > 0:
            self.current_hp += amount
            self.history.append(self.current_hp)
            print(f"HP {amount}를 회복했습니다. 현재 HP: {self.current_hp}")
        else:
            print("회복 값은 양수여야 합니다.")

    def undo(self):
        """
        가장 최근의 HP 변화를 되돌립니다.
        """
        if len(self.history) > 1:
            self.history.pop()
            self.current_hp = self.history[-1]
            print(f"상태를 되돌렸습니다. 현재 HP: {self.current_hp}")
        else:
            print("더 이상 되돌릴 상태가 없습니다.")
    
    def get_current_hp(self):
        return self.current_hp
                </pre>
            </div>
        </section>

        <section>
            <h2>기대 효과</h2>
            <ul>
                <li><strong>안정적인 이력 관리</strong>: HP 변화에 대한 모든 기록을 체계적으로 보존할 수 있습니다.</li>
                <li><strong>'되돌리기' 기능 구현</strong>: 스택의 특성을 활용하여 간단하게 되돌리기 기능을 추가할 수 있습니다.</li>
                <li><strong>개념의 시각화</strong>: 추상적인 스택 개념이 게임 로직이라는 구체적인 예시를 통해 명확하게 이해됩니다.</li>
            </ul>
        </section>
        
        <footer>
            <p style="text-align: center; font-size: 0.9em; color: #777; margin-top: 40px;">
                © 2025. 모든 권리 보유.
            </p>
        </footer>
    </div>

</body>
</html>
