package com.example.parcial

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.google.android.material.floatingactionbutton.FloatingActionButton

class ListarActividades : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_listar_actividades)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        val floating: FloatingActionButton = findViewById(R.id.showperson)
        floating.setOnClickListener{
            val intent = Intent (this, updateuser::class.java)
            startActivity(intent)
        }
        val data: FloatingActionButton = findViewById(R.id.add_data)
        data.setOnClickListener{
            val intent = Intent (this, home::class.java)
            startActivity(intent)
        }
    }
}