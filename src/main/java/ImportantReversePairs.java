public class ImportantReversePairs {
    public static int IRP(int[] nums){
        int count = 0;
        for (int i = 0; i < nums.length; ++i){//brute force approach through the array.
            for (int j =0 ; j < nums.length; ++j){
                if( i < j && nums[i] > 2* Math.abs(nums[j])){//the absolute value takes in the case there is a negative number in the array.
                    count++;
                }
            }
        }
        return count;
    }
}
