package com.example.communicate;


import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;


public class MainActivity extends AppCompatActivity {
    Button takeToMarksCalculation;
    Button taketoPDFS;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        takeToMarksCalculation = (Button) findViewById(R.id.takeToMarksCalculation);
        takeToMarksCalculation.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openMarksCalculationActivity();
            }
        });
        taketoPDFS = (Button) findViewById(R.id.takeToPDFS);
        taketoPDFS.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openPDFSOptionActivity();
            }
        });
    }
    public void openMarksCalculationActivity(){
        Intent intent = new Intent(this, MarksCalculation.class);
        startActivity(intent);
    }

    public void openPDFSOptionActivity(){
        Intent intent = new Intent(this, PDFSOption.class);
        startActivity(intent);
    }
}
