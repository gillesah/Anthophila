// import { Routes } from '@angular/router';

// export const routes: Routes = [];

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { BeeyardComponent } from './beeyard/beeyard.component';

export const routes: Routes = [{ path: '', component: BeeyardComponent }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
