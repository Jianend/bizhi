
public class sxh {
    public sxh(int a) {
        System.out.println(a);

    }

    public void sxh(int a) {
        // 获取a的长度
        int len = String.valueOf(a).length();
        // 创建一个数组，用于存放a的每一位数字
        int[] arr = new int[len];
        // 将a的每一位数字存放到数组中
        for (int i = 0; i < len; i++) {
            arr[i] = a % 10;
            a /= 10;
        }
        // 创建一个数组，用于存放a的每一位数字的平方
        int[] arr2 = new int[len];
        // 将a的每一位数字的长度次方存放到数组中
        for (int i = 0; i < len; i++) {
            arr2[i] = (int) Math.pow(arr[i], len);
        }
        // arr2数组的和
        int sum = 0;
        for (int i = 0; i < len; i++) {
            sum += arr2[i];
        }
        // 判断sum是否等于a
        if (sum == a) {
            System.out.println(a);
        }

    }

    public static void main(String[] args) {
        for (int a = 100; a <= 999; a++) {
            new sxh(a);
        }

    }
}