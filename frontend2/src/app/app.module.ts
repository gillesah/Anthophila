import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent // Assurez-vous d'avoir un AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule // Importation essentielle pour HttpClient
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
