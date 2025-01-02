import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt(); // 테스트 케이스 개수 입력
        sc.nextLine(); // 개행 문자 처리

        for (int i = 0; i < count; i++) {
            String str = sc.nextLine(); // 괄호 문자열 입력
            if (isValidParentheses(str)) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        sc.close();
    }

    private static boolean isValidParentheses(String str) {
        Stack<Character> stack = new Stack<>();

        for (int j = 0; j < str.length(); j++) {
            char ch = str.charAt(j);
            if (ch == '(') {
                stack.push(ch); // 왼쪽 괄호는 스택에 추가
            } else if (ch == ')') {
                if (stack.isEmpty()) {
                    return false; // 오른쪽 괄호가 나왔지만 스택이 비어 있으면 유효하지 않음
                }
                stack.pop(); // 짝을 맞췄으므로 스택에서 제거
            }
        }

        return stack.isEmpty(); // 모든 괄호가 짝이 맞으면 스택이 비어 있어야 함
    }
}
