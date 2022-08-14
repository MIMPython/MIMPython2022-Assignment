# File markdown assignment 02

## Nguyên lý Dependency Invertion - chữ D trong SOLID - một trong những cách thiết kế của OOP

### 1. Định nghĩa

Dependency Invertion (_Đảo ngược phụ thuộc_) là một nguyên lý trong thiết kế OOP. Nội dung của nó là:

1. Các module cấp cao không nên phụ thuộc vào các module cấp thấp, cả 2 nên phụ thuộc vào một module trừu tượng (interface)
2. Trừu tượng không nên phụ thuộc vào cụ thể, cụ thể nên phụ thuộc vào trừu tượng

### Ví dụ

Không tuân thủ nguyên lý Dependency Inversion, ví dụ dưới đây class EmployeeDetails phụ thuộc vào class SalaryCaculator(_object EmployeeDetail gọi đến object SalaryCalculator_)

```
public class SalaryCalculator
 {
     public float CalculateSalary(int hoursWorked, float hourlyRate) => hoursWorked * hourlyRate;
 }

 public class EmployeeDetails
 {
     public int HoursWorked { get; set; }
     public int HourlyRate { get; set; }
     public float GetSalary()
     {
         var salaryCalculator = new SalaryCalculator();
         return salaryCalculator.CalculateSalary(HoursWorked, HourlyRate);
     }
 }
```

Và chúng ta sửa lại theo cách áp dụng Dependency Inversion như sau:

```

    public interface ISalaryCalculator
    {
        float CalculateSalary(int hoursWorked, float hourlyRate);
    }

    public class SalaryCalculatorModified : ISalaryCalculator
    {
        public float CalculateSalary(int hoursWorked, float hourlyRate) => hoursWorked * hourlyRate;
    }

    public class EmployeeDetailsModified
    {
        private readonly ISalaryCalculator _salaryCalculator;
        public int HoursWorked { get; set; }
        public int HourlyRate { get; set; }
        public EmployeeDetailsModified(ISalaryCalculator salaryCalculator)
        {
            _salaryCalculator = salaryCalculator;
        }
        public float GetSalary()
        {
            return _salaryCalculator.CalculateSalary(HoursWorked, HourlyRate);
        }
    }
```

Class EmployeeDetail không còn phụ thuộc vào class SalaryCalculation nữa mà cả 2 class cùng phụ thuộc vào interface ISalaryCalculator
