package com.doctor3.basicandroid;

import android.os.Bundle;
import android.text.Editable;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {
    char[] enc = {0x19, 0x07, 0x00, 0x0e, 0x1b, 0x03, 0x10, 0x2f, 0x18, 0x02, 0x09, 0x3a, 0x04, 0x01, 0x3a, 0x2a, 0x0b, 0x1d, 0x06, 0x07, 0x0c, 0x09, 0x30, 0x54, 0x18, 0x3a, 0x1c, 0x15, 0x1b, 0x1c, 0x10};
    char[] key = {0x74, 0x68, 0x65, 0x6d, 0x6f, 0x65, 0x6b, 0x65, 0x79};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button check = findViewById(R.id.check);
        EditText input = findViewById(R.id.input);
        check.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String flag = input.getText().toString();
                if (flag.length() != 31) {
                    Toast.makeText(getApplicationContext(), "长度不对哦",
                            Toast.LENGTH_SHORT).show();
                    return;

                }
                byte[] bytes = flag.getBytes();
                for (int i = 0; i < 31; i++) {
                    if ((bytes[i] ^ key[i % (key.length)]) != enc[i]) {
                        Toast.makeText(getApplicationContext(), "好像有哪里不对",
                                Toast.LENGTH_SHORT).show();
                        return;
                    }
                }
                Toast.makeText(getApplicationContext(), "恭喜！回答正确",
                        Toast.LENGTH_SHORT).show();
            }
        });
    }

}