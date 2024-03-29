import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ServiceWorkerModule } from '@angular/service-worker';
import { environment } from '../environments/environment';
import { RoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CoreModule } from './core/core.module';
import { DemoModule } from './demo/demo.module';

@NgModule({
  declarations: [AppComponent],
  imports: [
    // Core Angular Module // Don't remove!
    CommonModule,
    BrowserAnimationsModule,

    // Fury Core Modules
    CoreModule,
    RoutingModule,
    DemoModule,

    // Register a Service Worker (optional)
    ServiceWorkerModule.register('/ngsw-worker.js', { enabled: environment.production })
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
