package com.example.communicate;


import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.res.AssetManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class PDFSOption extends AppCompatActivity {
   private static final int MY_PERMISSION_REQUEST_STORAGE=1;
  Button firstpdf;
  Button secondpdf;
  Button thirdpdf;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_p_d_f_s_option);

        if(ContextCompat.checkSelfPermission(PDFSOption.this, Manifest.permission.WRITE_EXTERNAL_STORAGE)!= PackageManager.PERMISSION_GRANTED){
            if(ActivityCompat.shouldShowRequestPermissionRationale(PDFSOption.this,Manifest.permission.WRITE_EXTERNAL_STORAGE)){
                ActivityCompat.requestPermissions(PDFSOption.this,new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},MY_PERMISSION_REQUEST_STORAGE);
            }else{
                ActivityCompat.requestPermissions(PDFSOption.this,new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE},MY_PERMISSION_REQUEST_STORAGE);
            }
        }else{

        }

        firstpdf = (Button) findViewById(R.id.firstPDF);
        firstpdf.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                copyAsset("1.pdf");
            }
        });
        secondpdf = (Button) findViewById(R.id.secondPDF);
        secondpdf.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                copyAsset("2.pdf");
            }
        });
        thirdpdf = (Button) findViewById(R.id.thirdPDF);
        thirdpdf.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                copyAsset("3.pdf");
            }
        });
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        switch (requestCode){
            case MY_PERMISSION_REQUEST_STORAGE:{
                if(grantResults.length>0&&grantResults[0]==PackageManager.PERMISSION_GRANTED){
                    if(ContextCompat.checkSelfPermission(PDFSOption.this,Manifest.permission.WRITE_EXTERNAL_STORAGE)==PackageManager.PERMISSION_GRANTED){

                    }
                }else{
                    Toast.makeText(this,"no permission granted",Toast.LENGTH_LONG).show();
                }
            }
        }
    }



    private void copyAsset(String filename ){
        String dirPath = Environment.getExternalStorageDirectory().toString()+"/Automatic_Answer_Grader/";
        Log.e("dirPATH",dirPath);
        File dir= new File(dirPath);
        if(!dir.exists()){
            dir.mkdirs();
        }
        AssetManager assetManager = getAssets();
        InputStream in =null;
        OutputStream out =null;
        try{
            in=assetManager.open(filename);
            File outFile = new File(dirPath,filename);
            out =new FileOutputStream(outFile);
            copyFile(in,out);
            Toast.makeText(this,"pdf is saved in Automatic_Answer_Grader folder of your storage",Toast.LENGTH_SHORT).show();
        }catch (IOException e){
            e.printStackTrace();
            Toast.makeText(this,"failed",Toast.LENGTH_SHORT).show();
        } finally {
            if(in != null){
                try {
                    in.close();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
            if(out != null){
                try {
                    out.close();
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }

    private void copyFile(InputStream in,OutputStream out ) throws IOException{
        byte[] buffer = new byte[1024] ;
        int read;
        while((read=in.read(buffer))!=-1){
            out.write(buffer,0,read);
        }
    }
}
