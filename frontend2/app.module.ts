import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HttpHandler } from '@angular/common/http';

@NgModule({
  imports: [BrowserModule, HttpClientModule],
  providers: [HttpHandler],
})
export class AppModule {}
