package com.example.communicate;

import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import android.widget.ImageView;
import android.widget.Toast;

import java.io.ByteArrayOutputStream;


import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import okhttp3.MediaType;
import okhttp3.MultipartBody;

import okhttp3.RequestBody;


public class MarksCalculation extends AppCompatActivity {
    Button captureEmptyOMR;
    Button captureAnsweredOMR;
    Button captureGroundOMR;
    Button uploadToServer;
    ImageView capturedEmptyOMR;
    ImageView capturedAnsweredOMR;
    ImageView capturedGroundOMR;
    ProgressDialog progressDialog;
    private static final int emptyOMR_pic_id = 123;
    private Bitmap emptyOMR_bitmap;
    private static final int answeredOMR_pic_id = 124;
    private Bitmap answeredOMR_bitmap;
    private static final int groundOMR_pic_id = 125;
    private Bitmap groundOMR_bitmap;
    byte[] emptyOMR_byteArray;
    byte[] answeredOMR_byteArray;
    byte[] groundOMR_byteArray;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_marks_calculation);
        captureEmptyOMR = (Button) findViewById(R.id.captureEmptyOmr);
        captureAnsweredOMR=(Button) findViewById(R.id.captureAnsweredOMR);
        captureGroundOMR = (Button) findViewById(R.id.captureGroundOMR);
        capturedEmptyOMR = (ImageView) findViewById(R.id.capturedEmptyOMR);
        capturedAnsweredOMR = (ImageView) findViewById(R.id.capturedAnsweredOMR);
        capturedGroundOMR = (ImageView) findViewById(R.id.capturedGroundOMR);
        uploadToServer = (Button) findViewById(R.id.uploadToServer);
        captureEmptyOMR.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent camera_intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(camera_intent,emptyOMR_pic_id);
            }
        });
        captureAnsweredOMR.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent camera_intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(camera_intent,answeredOMR_pic_id);
            }
        });
        captureGroundOMR.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent camera_intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(camera_intent,groundOMR_pic_id);
            }
        });
        uploadToServer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                uploadMultipleFiles();
            }
        });

    }
    protected void onActivityResult(int requestCode,
                                    int resultCode,
                                    Intent data) {

        // Match the request 'pic id with requestCode
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == emptyOMR_pic_id) {

            // BitMap is data structure of image file
            // which stor the image in memory
//            Uri picUri = data.getData();
            emptyOMR_bitmap= (Bitmap) data.getExtras()
                    .get("data");
//            bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), picUri);
//            uploadBitmap(bitmap);
            // Set the image in imageview for display
            capturedEmptyOMR.setImageBitmap(emptyOMR_bitmap);
            ByteArrayOutputStream stream = new ByteArrayOutputStream();
            emptyOMR_bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream);
            emptyOMR_byteArray = stream.toByteArray();
        }
        else if(requestCode == answeredOMR_pic_id)
        {
            // BitMap is data structure of image file
            // which stor the image in memory
//            Uri picUri = data.getData();
            answeredOMR_bitmap= (Bitmap) data.getExtras()
                    .get("data");
//            bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), picUri);
//            uploadBitmap(bitmap);
            // Set the image in imageview for display
            capturedAnsweredOMR.setImageBitmap(answeredOMR_bitmap);
            ByteArrayOutputStream stream = new ByteArrayOutputStream();
            answeredOMR_bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream);
            answeredOMR_byteArray = stream.toByteArray();
        }
        else if(requestCode == groundOMR_pic_id)
        {
            // BitMap is data structure of image file
            // which stor the image in memory
//            Uri picUri = data.getData();
            groundOMR_bitmap= (Bitmap) data.getExtras()
                    .get("data");
//            bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), picUri);
//            uploadBitmap(bitmap);
            // Set the image in imageview for display
            capturedGroundOMR.setImageBitmap(groundOMR_bitmap);
            ByteArrayOutputStream stream = new ByteArrayOutputStream();
            groundOMR_bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream);
            groundOMR_byteArray = stream.toByteArray();
        }
    }
    private void uploadMultipleFiles() {


        // Map is used to multipart the file using okhttp3.RequestBody
//        File file = new File(mediaPath);
//        File file1 = new File(mediaPath1);

        // Parsing any Media type file
//        RequestBody requestBody1 = RequestBody.create(MediaType.parse("*/*"), file);
//        RequestBody requestBody2 = RequestBody.create(MediaType.parse("*/*"), file1);
        RequestBody requestBody1 = RequestBody
                .create(emptyOMR_byteArray,MediaType.parse("application/octet-stream") );
        RequestBody requestBody2 = RequestBody
                .create(answeredOMR_byteArray,MediaType.parse("application/octet-stream") );
        RequestBody requestBody3 = RequestBody
                .create(groundOMR_byteArray,MediaType.parse("application/octet-stream") );

        MultipartBody.Part fileToUpload1 = MultipartBody.Part.createFormData("file1", "your_bitmap_file1.bmp", requestBody1);
        MultipartBody.Part fileToUpload2 = MultipartBody.Part.createFormData("file2", "your_bitmap_file2.bmp", requestBody2);
        MultipartBody.Part fileToUpload3 = MultipartBody.Part.createFormData("file3", "your_bitmap_file3.bmp", requestBody3);

        ApiConfig getResponse = AppConfig.getRetrofit().create(ApiConfig.class);
        Call<ServerResponse> call = getResponse.uploadMulFile(fileToUpload1, fileToUpload2,fileToUpload3);
        call.enqueue(new Callback<ServerResponse>() {
            @Override
            public void onResponse(Call<ServerResponse> call, Response<ServerResponse> response) {
                ServerResponse serverResponse = response.body();
                if (serverResponse != null) {
                    if (serverResponse.getSuccess()) {
                        Toast.makeText(getApplicationContext(), serverResponse.toString(), Toast.LENGTH_LONG).show();
//                        Log.e("response",serverResponse.getMessage());
                    } else {
                        Toast.makeText(getApplicationContext(), serverResponse.toString(), Toast.LENGTH_LONG).show();
//                        Log.e("response",serverResponse.getMessage());
                    }
                } else {
                    assert serverResponse != null;
                    Log.v("Response", serverResponse.toString());
                }

            }

            @Override
            public void onFailure(Call<ServerResponse> call, Throwable t) {
                Toast.makeText(getApplicationContext(),"API server work is pending",Toast.LENGTH_LONG).show();
            }
        });
    }
}
