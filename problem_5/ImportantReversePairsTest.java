import static org.junit.jupiter.api.Assertions.*;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

class ImportantReversePairsTest {

    @Test
    void IRP_test1() {
        int[] nums = new int[]{1,2,3,2,1};
        int actual = ImportantReversePairs.IRP(nums);
        System.out.println("First test is with: " + Arrays.toString(nums));
        System.out.println("Expected: 2");
        System.out.println("Actual: " + actual);
        Assert.assertEquals(1, actual);



    }

    @Test
    void IRP_test2(){
        int[] nums = new int[]{};
        int actual = ImportantReversePairs.IRP(nums);
        System.out.println("Second test is with: " + Arrays.toString(nums));
        System.out.println("Expected: 0");
        System.out.println("Actual: " + actual);
        Assert.assertEquals(0, actual);
    }

    @Test
    void IRP_test3(){
        int[] nums = new int[]{2,4,5,3,1};
        int actual = ImportantReversePairs.IRP(nums);
        System.out.println("Third test is with: " + Arrays.toString(nums));
        System.out.println("Expected: 3");
        System.out.println("Actual: " + actual);
        Assert.assertEquals(3, actual);
    }

    @Test
    void IRP_test4(){
        int[] nums = new int[]{9,9,3,121,-2};
        int actual = ImportantReversePairs.IRP(nums);
        System.out.println("Fourth test is with: " + Arrays.toString(nums));
        System.out.println("Expected: 0");
        System.out.println("Actual: " + actual);
        Assert.assertEquals(5, actual);
    }
}