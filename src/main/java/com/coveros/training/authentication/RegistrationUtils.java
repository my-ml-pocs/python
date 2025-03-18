package com.coveros.training.authentication;

public class RegistrationUtils {

    public static boolean isRegistrationValid(String username, String password) {
        // Example code with unnecessary boolean literal removed
        return (username != null && !username.isEmpty()) && (password != null && !password.isEmpty());
    }

}