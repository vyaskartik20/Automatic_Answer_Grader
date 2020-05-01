package com.example.communicate;

import com.google.gson.annotations.SerializedName;

public class ServerResponse {
    @SerializedName("success")
    boolean success;
    @SerializedName("message")
    String message;

    String getMessage() {
        return message;
    }

    boolean getSuccess() {
        return success;
    }

}