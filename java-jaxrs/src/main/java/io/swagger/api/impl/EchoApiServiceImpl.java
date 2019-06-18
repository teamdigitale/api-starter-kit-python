package io.swagger.api.impl;

import io.swagger.api.*;
import io.swagger.model.*;


import io.swagger.model.Problem;
import io.swagger.model.Timestamps;

import java.util.Date;
import java.util.List;

import java.io.InputStream;

import javax.ws.rs.core.Response;
import javax.ws.rs.core.SecurityContext;

@javax.annotation.Generated(value = "io.swagger.codegen.languages.java.JavaResteasyEapServerCodegen", date = "2019-05-29T07:22:35.356Z[Etc/UTC]")

public class EchoApiServiceImpl implements EchoApi {
  
      public Response getEcho(SecurityContext securityContext) {
      Timestamps ts = new Timestamps();
      ts.setTimestamp(new Date());
      return Response.ok(ts).build();
  }
  
}

