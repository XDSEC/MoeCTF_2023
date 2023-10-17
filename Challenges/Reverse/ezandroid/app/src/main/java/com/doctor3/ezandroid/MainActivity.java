package com.doctor3.ezandroid;

import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import com.doctor3.ezandroid.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {

    // Used to load the 'ezandroid' library on application startup.
    static {
        System.loadLibrary("ezandroid");
    }

    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        Button btn = findViewById(R.id.button);
        EditText input = findViewById(R.id.input);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String s = input.getText().toString();
                if (s.length() != 23) {
                    Toast.makeText(getApplicationContext(), "长度不对哦",
                            Toast.LENGTH_SHORT).show();
                    return;
                }
                if (check(s) == 1) { //ssaassssdddddwwddddwwaa
                    Toast.makeText(getApplicationContext(), "OK!RIGHT,flag is moectf{"+ s +"}",
                            Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(getApplicationContext(), "Try to reverse the native lib!",
                            Toast.LENGTH_SHORT).show();
                }
            }
        });

    }
    public native int check(String input);
}