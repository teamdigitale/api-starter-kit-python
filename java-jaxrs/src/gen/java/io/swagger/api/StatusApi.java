package io.swagger.api;

import io.swagger.model.*;

import io.swagger.annotations.ApiParam;
import io.swagger.jaxrs.*;

import io.swagger.model.Problem;


import java.util.List;
import java.util.Map;

import java.io.InputStream;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.SecurityContext;
import javax.ws.rs.*;

import javax.validation.constraints.*;


@Path("/status")


@io.swagger.annotations.Api(description = "the status API")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.java.JavaResteasyEapServerCodegen", date = "2019-05-29T07:45:52.500Z[Etc/UTC]")

public interface StatusApi  {
   

    @GET
    
    
    @Produces({ "application/problem+json" })
    @io.swagger.annotations.ApiOperation(value = "Ritorna lo stato dell'applicazione.", notes = "Ritorna lo stato dell'applicazione. A scopo di test, su base randomica puo' ritornare un errore. ", response = Problem.class, tags={ "public", })
    @io.swagger.annotations.ApiResponses(value = { 
        @io.swagger.annotations.ApiResponse(code = 200, message = "Il server ha ritornato lo status. In caso di problemi ritorna sempre un problem+json. ", response = Problem.class),
        
        @io.swagger.annotations.ApiResponse(code = 400, message = "Bad Request", response = Problem.class),
        
        @io.swagger.annotations.ApiResponse(code = 429, message = "Too many requests", response = Problem.class),
        
        @io.swagger.annotations.ApiResponse(code = 503, message = "Service Unavailable", response = Problem.class),
        
        @io.swagger.annotations.ApiResponse(code = 200, message = "Unexpected error", response = Problem.class) })
    public Response getStatus(@Context SecurityContext securityContext);

}

