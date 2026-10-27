import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

/**
 * Employee Salary Lookup using Map
 */
public class EmployeeSalaryLookup {

    static class Employee {
        String name;
        String department;
        double salary;

        Employee(String name, String department, double salary) {
            this.name = name;
            this.department = department;
            this.salary = salary;
        }
    }

    private final Map<Integer, Employee> employees = new TreeMap<>();

    public void addEmployee(int id, String name, String dept, double salary) {
        if (employees.containsKey(id)) {
            System.out.println("Employee ID " + id + " already exists.");
        } else if (salary <= 0) {
            System.out.p…
